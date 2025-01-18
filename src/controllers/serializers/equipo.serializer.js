import { z } from "zod";

export const crearEquipoSerializer = z.object({
    nombre: z.string(),
    estadio: z.string().optional(),
    imagenID: z.string().optional(),
})

export const actualizarEquipoSerializer = z.object({
    nombre: z.string().optional(),
    estadio: z.string().optional(),
})