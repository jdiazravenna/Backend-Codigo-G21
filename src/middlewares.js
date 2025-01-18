import JWT from "jsonwebtoken"
import {conexion} from "./conexion.js"
import { Tipo_usuario } from "@prisma/client"

export const validarUsuario = async (req, res, next) => { 
    // Si la informacion luego de validarla, cumple con todo, entonces dejaremos
    // pasar al siguiente controlador con la funcion next()

    // La informacion de las cabeceras de la peticion
    const { authorization } = req.headers

    if(!authorization){
        return res.status(403).json({
            message: "Se necesita una token para realizar esta peticion"
        })
    }
    // En el header de autorization, debe de enviar la token en el siguiente formato
    // bearer xxx.yyyy.zzzzz
    const token = authorization.split(" ")[1]
    // ['Bearer', 'xxxx,yyyy.zzzz']

    if(!token){
        return res.status(403).json({
            message: "El formato de la token, debe ser Bearer YOUR_TOKEN"
        })
    }
    // El payload devolverá toda la informacion q le colocamos al momento de crear la token
    const payload = JWT.verify(token, process.env.SECRET_KEY)
    const usuarioEncontrado = await conexion.usuario.findUniqueOrThrow({
        where: { id: payload.usuarioId}
    })
    // Dentro del req (request) podemos agregar informacion
    req.user = usuarioEncontrado
    next()
}

export const validarAdmin = async (req, res, next) => {
    // req.user
    console.log(req.user)
    if(req.user.tipo_usuario === Tipo_usuario.ADMIN){
        next()

    }else{
        return res.json({
            message: `El usuario tiene q ser ${Tipo_usuario.ADMIN} para realizar esta acción`
        })
    }
}