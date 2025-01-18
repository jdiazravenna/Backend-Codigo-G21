import {z} from "zod"
import { Tipo_usuario } from "@prisma/client"

export const registrarUsuarioSerializer = z.object({
    email: z.string().email(),
    password: z.string().regex(
        /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!*&%?#])[A-Za-z\d@$!*&%?#]{8,}$/),
    
    tipoUsuario: z.enum([
        Tipo_usuario.ADMIN,
        Tipo_usuario.MODERADOR,
        Tipo_usuario.USUARIO,
    ]),
    nombre: z.string().optional(),
    apellido: z.string().optional()
})

export const loginSerializer = z.object({
    email: z.string().email(),
    password: z.string()
})

export const actualizarUsuarioSerializer = z.object({
    nombre: z.string().optional(),
    apellido: z.string().optional()

})

