import {conexion} from "../conexion.js"
import { equipoEnrutador } from "../routes/equipo.routes.js"
import {
    crearEquipoSerializer, 
    actualizarEquipoSerializer} from "./serializers/equipo.serializer.js"
import { paginationSerializer } from "../utils.js"

export const crearEquipo = async (req, res) => {
    const data = req.body
    const dataValidada = crearEquipoSerializer.parse(data)

    const nuevoEquipo = await conexion.equipo.create({data: dataValidada})

    return res.json({
        message: "Equipo creado exitosamente",
        content: nuevoEquipo
    })

}
export const actualizarEquipo = async (req, res) => {
    console.log(req.params)
    const dataValidada = actualizarEquipoSerializer.parse(req.body)
    const equipoActualizado = await conexion.equipo.update({
        
        data: dataValidada,
        select: {
            id: true,
            nombre: true,
            estadio: true,
        },
        where: {
            id: Number(req.params.id) // convertir de string a number
            // params para obtener los parametros para actualizar el equipo y lo convertimos a number
        }
    })
    return res.json({
        message: "Equipo Actualizado correctamente",
        content: equipoActualizado
    })
}

export const listarEquipos = async (req, res) => {
    console.log(req.query)
    // Paginacion
    const { page, perPage} = req.query
    let skip, take
    if (page && perPage) {
        // skip > cuantos elementos se debe de saltar
        skip = (Number(page) -1)* Number(perPage)
        // take > cuantos elementos se debe tomar luego de saltarse
        take = Number(perPage)
    }

    const filtros = {}
    if (req.query.nombre){
        // Si queremos hacer la busqueda mediante una similitud del resultado, saumos contains
        filtros.nombre = { contains: req.query.nombre }

    }
    if (req.query.estadio){
        filtros.estadio = { contains: req.query.estadio }
    }
    // Crear el controlador para listar todos los equipos
    // Cualquier usuario (identificado  ono) puede acceder a esta informacion
    const equipos = await conexion.equipo.findMany({
        where: filtros,
        skip,
        take,
    })

    const totalEquipos = await conexion.equipo.count({
        where: filtros,
    })
    const pageInfo = paginationSerializer(
        totalEquipos,
        Number(page),
        Number(perPage)
    )

    return res.json({
        content: equipos,
        pageInfo
    })
}