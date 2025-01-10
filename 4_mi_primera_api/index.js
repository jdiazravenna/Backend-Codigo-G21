import express from 'express'

// colocamos en la variable servidor, express, para que sea un servidor express
const servidor = express()

// Configurar lo q podemos recibir por el body
// express.json() > indicamos que el contenido que podemos recibir por el body puede ser en formato application/json
servidor.use(express.json())
// Sera otro formato para recibir informacion por el body, en formato x-www-url-encoded
// DEPRECADO: ya no se recomienda utilizar
// servidor.user(express.urlencoded())

servidor.use(express.urlencoded())
// para recibir pior el body puro texto
servidor.use(express.text())

// Express no puede reiniciar el servidor automaticamente, para eso se necesita una libreria nodemon
servidor.get('/', (get, resp) => {
    resp.json({
        message: "Bienvenido a mi API",
    })
})

servidor.post('/crear-usuario', (req, resp) => {
    // req.body es todo el cuerpo que me envia el cliente
    console.log(req.body)

    resp.json({
        message: "Usuario creado exitosamente"
    })
})

// hacemos el llamado al servidor y colocamos el puerto 3000
servidor.listen(3000, () => {
    console.log("Servidor corriendo exsitosamente")
})
