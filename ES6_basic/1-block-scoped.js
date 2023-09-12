export default function taskBlock(trueOrFalse) {
    const task = false;
    const task2 = true;
  
    if (trueOrFalse) {
      const task1InsideBlock = true;
      const task2InsideBlock = false;
    }
  
    return [task, task2];
  }