import { userStore, type User, questionStore } from '@/stores';
import { io } from 'socket.io-client';

export function initializeConnection(user: User) {
  const socket = io('/');
  userStore.updateServerConnection(socket);

  // User Callbacks
  socket.on('users', userStore.updateUsers);
  socket.on('answers', userStore.updateAnswers);
  socket.on('buzzers', userStore.updateBuzzers);

  // Question Callbacks
  socket.on('question', questionStore.updateQuestion);
  socket.on('solution', questionStore.updateSolution);

  // Register with username and role
  socket.emit('login', user);
}
