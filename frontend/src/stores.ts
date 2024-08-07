import { reactive } from 'vue';
import { Socket } from 'socket.io-client';

export type User = {
  name: string;
  role: 'Player' | 'Moderator';
  buzzerActive: boolean;
  answer: string;
};

function applyToUsers<T extends keyof User>(values: { name: string; value: User[T] }[], propName: T) {
  values.forEach((value) => {
    const user = userStore.users.find((user) => user.name === value.name);
    if (user) {
      user[propName] = value.value;
    } else {
      console.error(`Could not find User with name ${value.name}`);
    }
  });
}

export const userStore = reactive({
  users: [] as User[],
  serverConnection: undefined as any,

  updateUsers(users: User[]) {
    userStore.users = users;
  },

  updateServerConnection(serverConnection: Socket) {
    userStore.serverConnection = serverConnection;
  },

  updateAnswers(answers: { name: string; value: string }[]) {
    applyToUsers(answers, 'answer');
  },

  updateBuzzers(buzzers: { name: string; value: boolean }[]) {
    applyToUsers(buzzers, 'buzzerActive');
  },
});

type Question = {
  number: number;
  question: {
    type: 'text';
    text: string;
  };
  input: {
    type: 'buzzer' | 'textInput';
  };
  solution?: {
    type: 'text';
    text: string;
  };
};

export const questionStore = reactive({
  question: undefined as Question | undefined,

  updateQuestion(question: Question) {
    questionStore.question = question;
    questionStore.question.solution = undefined;
  },

  updateSolution(solution: { type: 'text'; text: string }) {
    if (questionStore.question) questionStore.question.solution = solution;
  },
});
