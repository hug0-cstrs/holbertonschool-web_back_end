export default function taskBlock(trueOrFalse) {
    const task = false;
    const task2 = true;
  
    if (trueOrFalse) {
      // eslint-disable-next-line no-unused-vars
      const taskInsideBlock = true;
      // eslint-disable-next-line no-unused-vars
      const task2InsideBlock = false;
    }
  
    return [task, task2];
  }