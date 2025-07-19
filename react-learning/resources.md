# Core React Concepts

- What is React and what are its key features?
React is an open-source JavaScript library for building user interfaces (UIs), primarily for single-page applications (SPAs). Developed by Facebook (now Meta), React allows developers to create reusable UI components that update efficiently when data changes.
Key Features of React
1. Component-Based Architecture
React apps are built using reusable components (like Lego blocks).
Each component manages its own state and logic.
Example:
function Button() {
  return <button>Click Me</button>;
}

2. Virtual DOM (Document Object Model)
React uses a Virtual DOM (a lightweight copy of the real DOM).
Changes are first applied to the Virtual DOM, then React efficiently updates only the necessary parts of the real DOM (reducing performance bottlenecks).


- Explain the Virtual DOM and how it works.

- What is JSX? How is it different from HTML?

- What are the differences between React and Angular/Vue?

- What are React components? Explain functional vs. class components.

- What are props in React? How do you pass them?

- What is state in React? How is it different from props?

- What are controlled and uncontrolled components?

- What are keys in React and why are they important?

- What are React Fragments and why use them?

# React Hooks

- What are React Hooks? Why were they introduced?

- Explain useState and how it works.

- Explain useEffect and its dependency array.

- What is useContext and when would you use it?

- Explain useRef and its common use cases.

- What is useMemo and how does it optimize performance?

- What is useCallback and how is it different from useMemo?

- What are custom hooks? How do you create one?

- What are the rules of hooks?

- Can hooks be used inside class components? Why or why not?

# React Lifecycle Methods (Class Components)

- What are React lifecycle methods?

- Explain componentDidMount, componentDidUpdate, and componentWillUnmount.

- What is shouldComponentUpdate and how is it used for optimization?

- What is getDerivedStateFromProps?

- What is getSnapshotBeforeUpdate?

# State Management

- What is state management in React?

- What is the Context API and when should you use it?

- What is Redux? How does it work?

- Explain Redux actions, reducers, and store.

- What is middleware in Redux? (e.g., Redux Thunk, Redux Saga)

- What is MobX and how does it compare to Redux?

- What is React Query and when would you use it?

- What is Zustand and how does it compare to Redux?

- How do you handle global state without Redux?

- What is the difference between state lifting and Context API?

# React Router

- What is React Router and how does it work?

- Explain <BrowserRouter>, <Route>, <Link>, and <Switch>.

- How do you handle dynamic routing in React?

- How do you implement protected routes?

- What is the difference between useNavigate and useHistory?

# Performance Optimization

- How do you optimize React performance?

- What is React.memo and how does it work?

- How does useMemo optimize performance?

- How does useCallback optimize performance?

- What is lazy loading and how do you implement it in React?

- What is code splitting and how do you achieve it?

- How do you handle large lists efficiently in React?

- What is the significance of the key prop in lists?

- How do you prevent unnecessary re-renders in React?

- What is server-side rendering (SSR) and how does it help performance?

# Error Handling & Debugging

- How do you handle errors in React components?

- What are Error Boundaries in React?

- How do you debug a React application?

- What is StrictMode in React and why is it used?

- How do you log and monitor errors in production?

# React Patterns & Best Practices

- What are Higher-Order Components (HOCs)?

- What are Render Props and how do they work?

- What is the Compound Component pattern?

- What is the Provider Pattern in React?

- What are Controlled vs. Uncontrolled Components?

- How do you handle forms in React?

- What is prop drilling and how do you avoid it?

- How do you structure a large React application?

- What are Pure Components in React?

- How do you implement authentication in React?

# Advanced React Concepts

- What is React Fiber?

- How does React handle reconciliation?

- What are Portals in React and when would you use them?

- What is Suspense in React?

- How do you implement animations in React?

- What is Concurrent Mode in React?

- What is Server Components in React?

- How do you test React components?

- What are React hooks limitations?

- How does React differ from React Native?

# React Testing

- What tools do you use to test React applications?

- How do you test React components using Jest?

- What is React Testing Library and how do you use it?

- How do you mock API calls in React tests?

- What is snapshot testing in React?

# React & TypeScript

- How do you use TypeScript with React?

- How do you type React props in TypeScript?

- How do you type React hooks in TypeScript?

- How do you type React events in TypeScript?

- What are the benefits of using TypeScript with React?

# React Ecosystem & Tools

- What is Next.js and how does it differ from React?

- What is Gatsby and when would you use it?

- What is Create React App (CRA) and its alternatives?

- How do you deploy a React application?

- What is Webpack and how does it work with React?

- What is Babel and why is it used in React?

- What is ESLint and how do you configure it for React?

- What is Prettier and how does it help in React development?

- How do you handle environment variables in React?

- What is Storybook and why is it useful?

# React Interview Scenarios

- How do you implement a search filter in React?

- How do you implement infinite scrolling in React?

- How do you implement drag-and-drop in React?

- How do you implement a dark/light theme toggle in React?

- How do you optimize a slow React application?

###################################################################

### 100 Important JavaScript Interview Questions ###
JavaScript Fundamentals
What is JavaScript and how does it differ from Java?

What are the data types in JavaScript?

What is the difference between let, const, and var?

What is hoisting in JavaScript?

What is the difference between == and ===?

What is NaN and how do you check for it?

What is the difference between null and undefined?

What is the typeof operator and how does it work?

What are truthy and falsy values in JavaScript?

What is the difference between function declaration and function expression?

Functions & Scope
What is a closure in JavaScript? Give an example.

What is the this keyword and how does it work?

How do you change the context of this (call, apply, bind)?

What is an arrow function and how is it different from a regular function?

What is a higher-order function?

What is a callback function?

What is a pure function?

What is an IIFE (Immediately Invoked Function Expression)?

What is the difference between function foo() {} and const foo = () => {}?

What is lexical scope in JavaScript?

Objects & Prototypes
How do you create an object in JavaScript?

What is object destructuring?

What is the difference between shallow copy and deep copy?

What is the prototype chain in JavaScript?

What is Object.create()?

What is the difference between __proto__ and prototype?

What are getters and setters in JavaScript?

How do you check if an object has a property?

What is the difference between Object.keys() and Object.getOwnPropertyNames()?

How do you merge two objects in JavaScript?

Arrays & Array Methods
What are the common array methods in JavaScript?

What is the difference between map, filter, and reduce?

How do you remove duplicates from an array?

What is the difference between slice and splice?

How do you flatten a nested array?

What is the difference between forEach and map?

How do you check if an array includes a value?

How do you sort an array in JavaScript?

What is the spread operator and how is it used with arrays?

How do you convert an array-like object to an array?

Asynchronous JavaScript
What is asynchronous JavaScript?

What is a callback hell and how do you avoid it?

What are Promises in JavaScript?

What is async/await and how does it work?

What is the difference between Promise.all and Promise.race?

How do you handle errors in Promises?

What is the event loop in JavaScript?

What are microtasks and macrotasks?

What is setTimeout and how does it work?

What is the difference between setTimeout and setInterval?

ES6+ Features
What are template literals?

What are default parameters?

What are rest and spread operators?

What are destructuring assignments?

What are arrow functions and their benefits?

What are let and const in ES6?

What are Symbols in JavaScript?

What are Map and Set in JavaScript?

What are generators in JavaScript?

What are modules in ES6 (import/export)?

Error Handling & Debugging
What are the different types of errors in JavaScript?

How do you handle errors using try-catch?

What is throw in JavaScript?

How do you debug JavaScript code?

What is console.log vs console.error vs console.warn?

DOM Manipulation & Events
What is the DOM in JavaScript?

How do you select elements in the DOM?

How do you create and append elements in the DOM?

What is event delegation?

What is the difference between event.preventDefault() and event.stopPropagation()?

How do you add and remove event listeners?

What are the different ways to handle events in JavaScript?

What is the difference between window.onload and DOMContentLoaded?

What is the difference between innerHTML and textContent?

How do you handle forms in JavaScript?

Advanced JavaScript Concepts
What is memoization in JavaScript?

What is currying in JavaScript?

What is the Module Pattern in JavaScript?

What is the Revealing Module Pattern?

What is the Singleton Pattern in JavaScript?

What is the Observer Pattern in JavaScript?

What is the Factory Pattern in JavaScript?

What is the Prototype Pattern in JavaScript?

What is the difference between composition and inheritance?

What is the difference between imperative and declarative programming?

JavaScript Testing & Tools
What is Jest and how do you use it?

What is Mocha and Chai?

What is unit testing in JavaScript?

What is mocking in JavaScript testing?

What is ESLint and how do you use it?

JavaScript Security & Best Practices
What is XSS (Cross-Site Scripting) and how do you prevent it?

What is CORS and how does it work?

What is CSRF (Cross-Site Request Forgery) and how do you prevent it?

What are some JavaScript security best practices?

What is strict mode in JavaScript?

JavaScript Interview Scenarios
How do you reverse a string in JavaScript?

How do you check if a string is a palindrome?

How do you find the largest number in an array?

How do you implement a debounce function?

How do you implement a throttle function?

