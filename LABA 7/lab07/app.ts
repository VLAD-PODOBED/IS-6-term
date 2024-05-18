import express from 'express';
//import {decrypt, encrypt} from "./des";
import {avalancheEffect, decrypt, encrypt} from "./des";
const app = express();

app.use(express.json());
app.use(express.urlencoded({extended: false}));
app.set('view engine', 'ejs');

app.get("/", (req, res) => {
    res.render('des');
});

// app.post("/encrypt", (req, res) => {
//     let startTime = performance.now();
//     let encryptedText = encrypt(req.body.enc_text);
//     let endTime = performance.now();
//     const encodingTime = (endTime - startTime).toFixed(4);


//     res.status(200).json({
//         result: encryptedText,
//         encodingTime: encodingTime
//     });
// });

app.post("/encrypt", (req, res) => {
    let startTime = performance.now();
    let encryptedText = encrypt(req.body.enc_text);
    let endTime = performance.now();
    const encodingTime = (endTime - startTime).toFixed(4);

    const avalanche = avalancheEffect(req.body.enc_text);

    res.status(200).json({
        result: encryptedText,
        avalanche: avalanche,
        encodingTime: encodingTime
    });
});

app.post("/decrypt", (req, res) => {
    let startTime = performance.now();
    let decryptedText = decrypt(req.body.dec_text);
    let endTime = performance.now();
    const decodingTime = (endTime - startTime).toFixed(4);

    res.status(200).json({
        result: decryptedText,
        decodingTime: decodingTime
    });
});


app.listen(3000, () => console.log(`Server is running at http://localhost:3000`));