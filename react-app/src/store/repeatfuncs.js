export const movieIs = (string) => {
    const words = string.split(',');
    let newWords = [];
    for (let i = 0; i < words.length - 1; i++) {
      newWords.push(words[i], " · ");
    }
    newWords.push(words[words.length - 1])
    return newWords.join("")
  };

