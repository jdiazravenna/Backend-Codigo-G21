import express from "express"
import asyncHandler from "express-async-handler"
import { actualizarEquipo, crearEquipo, listarEquipos } from "../controllers/equipo.controller.js"
import { validarAdmin, validarUsuario } from "../middlewares.js"

export const equipoEnrutador = express()

equipoEnrutador.route("/equipo").post(
    asyncHandler(validarUsuario),
    asyncHandler(validarAdmin),
    asyncHandler(crearEquipo))

equipoEnrutador.put("/actualizar-equipo/:id", asyncHandler(actualizarEquipo))
equipoEnrutador.route('/equipos').get(asyncHandler(listarEquipos))

