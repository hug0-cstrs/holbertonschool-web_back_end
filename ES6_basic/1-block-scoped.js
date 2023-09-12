export default function taskBlock(trueOrFalse) {
    var task = false;
    var task2 = true;
  
    if (trueOrFalse) {
        const task1InsideBlock = true;
        const task2InsideBlock = true;
    }
  
    return [task, task2];
  }
