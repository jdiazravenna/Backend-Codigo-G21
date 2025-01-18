import { genSalt, hash, compare } from "bcrypt"
import { registrarUsuarioSerializer, loginSerializer, actualizarUsuarioSerializer } from "./serializers/usuario.serializer.js" 
import { conexion } from "../conexion.js"
import JWT from "jsonwebtoken"

export const registrarUsuario = async (req, res) => {
    const data = req.body
    
    // valida si la informacion es valida o no
    const dataValidada = registrarUsuarioSerializer.parse(data)
    console.log(dataValidada)

    const salt = await genSalt()
    const password = await hash(dataValidada.password, salt)

    const nuevoUsuario = await conexion.usuario.create({
        data: {
            email: dataValidada.email,
            apellido: dataValidada.apellido,
            nombre: dataValidada.nombre,
            password,
            tipo_usuario: dataValidada.tipoUsuario,
        },

        select: {
            id: true,
            email: true,
            apellido: true,
            nombre: true,
            tipo_usuario: true,
        }
    })

    return res.json({
        message: "usuario registrado exitosamente",
        content: nuevoUsuario
    })
}

export const login = async (req, res) => {
    const dataValidada = loginSerializer.parse(req.body)

    const usuarioEncontrado = await conexion.usuario.findUniqueOrThrow({
        where: { email: dataValidada.email}
    })
    const esLaPassword = await compare(
        dataValidada.password, 
        usuarioEncontrado.password
    )
    if (esLaPassword){
        const token = JWT.sign(
            { usuarioId: usuarioEncontrado.id },
            process.env.SECRET_KEY,
            {
                expiresIn: 60*60*4 // es 4 horas
                // "2 days" , "12h", 1h
            }
        )
        return res.json({
            message: "Bienvenido",
            content: token
        })
    }else{
        return res.status(403).json({
            message: "Credenciales incorrectas"
        })
    }
}

export const actualizarUsuario = async (req, res) => {
    // req.user tiene toda la informacion del usuario registrado
    // Actualizar mi usuario
    // Crea un serializador para poder recibir el nombre o apellido
    const dataValidada = actualizarUsuarioSerializer.parse(req.body)
    const usuarioActualizado = await conexion.usuario.update({
        data: dataValidada,
        select: {
            id: true,
            nombre: true,
            apellido: true,
            email: true,
            tipo_usuario: true,
        },
        where: {
            id: req.user.id,
        }
    })
    return res.json({
        message: "usuario actualizado exitosamente",
        content: usuarioActualizado
    })
}
export const devolverUsuario = async (req, res) => {
    return res.json({
        content: req.user
    })
}