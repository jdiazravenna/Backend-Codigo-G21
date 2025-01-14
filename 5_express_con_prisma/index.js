import express from 'express'
// Esta libreria se agrega cuando creamos los tipos de prisma
// npx prisma migrate generate
// cuando creamos una nueva migracion y se ejecuta en la bd
import Prisma from "@prisma/client"

const conexion = new Prisma.PrismaClient()
const servidor = express()
// indicamos que el servidor va a recibir un json
servidor.use(express.json())

servidor.post('/registro', async (req, res) => {
    try{
        const data = req.body // { nombre: "", email: "", nickName:""}

        // Resultado > seria la ejecucion correcta de la funcion
        const resultado = await conexion.usuario.create({
            data // {nombre: data.nombre, email: data.email, nickName: data.nickName}
        })
        // Aca pones tu mensaje
        return res.json({
            message: "usuario creado correctamente",
            content: resultado
        })
    }catch(error) {
        // Obtenemos el error de la ejecucion del proceso asincrono
        if (error instanceof Prisma.Prisma.PrismaClientValidationError){
            console.log(error)
            return res.json({
                message: "Error al hacer la peticion a la BD"
            })
        }
        return res.json({
            message: "Error al crear el usuario"
        })
    }
})

servidor.route('/notas')
.post(async (req, res)=>{
    const data = req.body
    try{
        const notaCreada = await conexion.nota.create({ data })
        
        return res.json({
            message: "Nota creada exitosamente",
            content: notaCreada
        })
    }catch (error) {
        // console.log(error)
        
     return res.json({
        message: "Error al crear la nota"
     })
        
    }
}).get(async (req, res)=>{
    const notas = await conexion.nota.findMany()
    return res.json({
        content: notas
    })
})

servidor.listen(process.env.PORT,()=>{
    console.log(
        `Servidor corriendo exitosamente en el puerto ${process.env.PORT}`
    )
})