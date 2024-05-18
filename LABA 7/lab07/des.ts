import CryptoJS from "crypto-js";

const ALGORITHM_KEY = "0b01FE";
//0b01FE 

export const encrypt = (plainText: string) => {
    return CryptoJS.DES.encrypt(plainText, ALGORITHM_KEY).toString();
}

export const decrypt = (encryptedText: string) => {
    const decryptedBytes = CryptoJS.DES.decrypt(encryptedText, ALGORITHM_KEY);
    return decryptedBytes.toString(CryptoJS.enc.Utf8);
}

export const avalancheEffect = (originalText: string) => {
    let changedBits: number = 0;

    const encryptedText1: string = convertStringToBinary(encrypt(originalText));

    let stringWithOneBitChanged = invertLastBit(convertStringToBinary(originalText));
    const encryptedText2: string = convertStringToBinary(encrypt(stringWithOneBitChanged));

    for (let i = 0; i < encryptedText1.length; i++) {
        if (encryptedText1[i] !== encryptedText2[i]) {
            changedBits++;
        }
    }

    return changedBits / encryptedText1.length * 100;
}

const invertLastBit = (binaryString: string): string => {
    const lastBit = binaryString[binaryString.length - 1];
    const invertedLastBit = lastBit === "0" ? "1" : "0";
    return binaryString.slice(0, -1) + invertedLastBit;
}


const convertStringToBinary = (str: string): string => {
    let binaryString = "";
    for (let i = 0; i < str.length; i++) {
        let charCode = str.charCodeAt(i).toString(2);
        charCode = charCode.length < 8 ? charCode.padStart(8, '0') : charCode;
        binaryString += charCode;
    }

    return binaryString;
}

const convertBinaryToString = (binaryString: string): string => {
    let text = '';
    for (let i = 0; i < binaryString.length; i += 8) {
        const byte = binaryString.slice(i, i + 8);
        const charCode = parseInt(byte, 2);
        const char = String.fromCharCode(charCode);
        text += char;
    }
    return text;
}
