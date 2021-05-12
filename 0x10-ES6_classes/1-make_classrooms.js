import ClassRoom from './0-classroom.js';

export default function initializeRooms() {
  const array = [];
  const room1 = new ClassRoom(19);
  const room2 = new ClassRoom(20);
  const room3 = new ClassRoom(34);
  array.push(room1, room2, room3);
  console.log(array);
}
