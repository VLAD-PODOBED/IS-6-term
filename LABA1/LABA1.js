const fs = require('fs');
// Функция для расчета энтропии алфавита
function calculateEntropy(frequencies) {
  const totalSymbols = Object.values(frequencies).reduce((sum, freq) => sum + freq, 0);
  let entropy = 0;
  for (const freq of Object.values(frequencies)) {
    const probability = freq / totalSymbols;
    entropy -= probability * Math.log2(probability);
  }
  return entropy;
}
// Функция для подсчета частоты символов в текстовом файле
function countCharacterFrequencies(filename) {
  const text = fs.readFileSync(filename, 'utf8');
  const frequencies = {};
  for (const char of text) {
    if (frequencies[char]) {
      frequencies[char]++;
    } else {
      frequencies[char] = 1;
    }
  }
  return frequencies;
}
// Функция для создания гистограммы частот символов
function createHistogram(frequencies) {
  const histogram = [];
  for (const [char, freq] of Object.entries(frequencies)) {
    histogram.push(`${char}: ${freq}`);
  }
  return histogram;
}
// Задание алфавитов и файлов для анализа
const alphabets = {
    'голландский (латиница)': './text_golland.txt',
    'украинский (кириллица)': './text_ukraina.txt',
    'бинарный алфавит': './binary_data.txt'
  }; 
  // а) Расчет энтропии указанных алфавитов
  for (const [alphabet, file] of Object.entries(alphabets)) {
    console.log(`Алфавит: ${alphabet}`);
    const isBinaryAlphabet = alphabet === 'бинарный алфавит';
    const data = isBinaryAlphabet ? fs.readFileSync(file) : fs.readFileSync(file, 'utf8');
    const frequencies = countCharacterFrequencies(data, isBinaryAlphabet);
    console.log('Частоты появления символов:');
    console.log(createHistogram(frequencies));
    const entropy = calculateEntropy(frequencies);
    console.log(`Энтропия алфавита: ${entropy.toFixed(4)}`);
    console.log('--------------------------');
  }
  // в) Подсчет количества информации в сообщении, состоящем из собственной фамилии, имени и отчества

  const name = 'Podobed Vladislav Georgievich';

  const asciiName = name.split('').map(char => char.charCodeAt(0));
  const entropyName = calculateEntropy(countCharacterFrequencies(name));
  const entropyASCII = calculateEntropy(countCharacterFrequencies(asciiName));

  console.log(`Количество информации в сообщении "${name}" (исходный алфавит):`);
  console.log(`Байт: ${name.length}`);
  console.log(`Бит: ${name.length * 8 * entropyName.toFixed(4)}`);
  console.log('--------------------------');

  console.log(`Количество информации в сообщении "${asciiName}" (ASCII):`);
  console.log(`Байт: ${asciiName.length}`);
  console.log(`Бит: ${asciiName.length * 8 * entropyASCII.toFixed(4)}`);
  console.log('--------------------------');

  const ukrainianName = 'Подобед Владислав Георгійович';

  const ukrainianAsciiName = ukrainianName.split('').map(char => char.charCodeAt(0));
  const entropyUkrainianName = calculateEntropy(countCharacterFrequencies(ukrainianName));
  const entropyUkrainianASCII = calculateEntropy(countCharacterFrequencies(ukrainianAsciiName));

  console.log(`Количество информации в сообщении "${ukrainianName}" (исходный алфавит):`);
  console.log(`Байт: ${ukrainianName.length}`);
  console.log(`Бит: ${ukrainianName.length * 8 * entropyUkrainianName.toFixed(4)}`);
  console.log('--------------------------');

  console.log(`Количество информации в сообщении "${ukrainianAsciiName}" (ASCII):`);
  console.log(`Байт: ${ukrainianAsciiName.length}`);
  console.log(`Бит: ${ukrainianAsciiName.length * 8 * entropyUkrainianASCII.toFixed(4)}`);
  console.log('--------------------------');

  // г) Подсчет количества информации в сообщении с учетом вероятности ошибочной передачи
  const errorProbabilities = [0.1, 0.5, 1.0];
  for (const errorProbability of errorProbabilities) {
    const errorCorrectedBitCount = name.length * 8 * (1 - errorProbability);
    console.log(`Количество информации в сообщении "${name}" с учетом вероятности ошибки ${errorProbability}:`);
    console.log(`Байт: ${errorCorrectedBitCount / 8}`);
    console.log(`Бит: ${errorCorrectedBitCount}`);
    console.log('--------------------------');
  }
  
 function countCharacterFrequencies(data, isBinary) {
    const frequencies = {}; 
    if (isBinary) {
      for (const byte of data) {
        const key = byte.toString();
        if (frequencies[key]) {
          frequencies[key]++;
        } else {
          frequencies[key] = 1;
        }
      }
    } else {
      for (let i = 0; i < data.length; i++) {
        const char = data[i];
        const key = char;
        if (frequencies[key]) {
          frequencies[key]++;
        } else {
          frequencies[key] = 1;
        }
      }
    }
    return frequencies;
  } 