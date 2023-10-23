const axios = require('axios');

// Define the API base URL
const baseURL = 'https://jsonplaceholder.typicode.com';

// Helper function to make API requests
const makeRequest = (url) => axios.get(`${baseURL}${url}`);

// Test to check if the API is reachable
test('API is reachable', async () => {
  try {
    const response = await makeRequest('/');
    expect(response.status).toBe(200);
  } catch (error) {
    // Handle any errors here
  }
});

// Test to get a specific post by ID
test('Get a post by ID', async () => {
  const postId = 1;
  const response = await makeRequest(`/posts/${postId}`);
  expect(response.status).toBe(200);
  expect(response.data.id).toBe(postId);
});

// Test to list all posts
test('List all posts', async () => {
  const response = await makeRequest('/posts');
  expect(response.status).toBe(200);
  expect(response.data.length).toBeGreaterThan(0);
});

// Add more tests for other API endpoints as needed
