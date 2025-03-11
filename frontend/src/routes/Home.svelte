<script lang="ts">
  import { Link } from 'svelte-navigator';
</script>

<div class="py-12">
  <div class="text-center mb-12">
    <h1 class="text-4xl font-bold text-gray-900 mb-4">
      Svelte + FastAPI + Tailwind Template
    </h1>
    <p class="text-xl text-gray-600 max-w-2xl mx-auto">
      A modern web application template with Svelte for the frontend, 
      FastAPI for the backend, and Tailwind CSS for styling.
    </p>
  </div>
  
  <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mt-12">
    <div class="bg-white p-6 rounded-lg shadow-md">
      <h2 class="text-xl font-semibold text-primary-600 mb-3">Svelte</h2>
      <p class="text-gray-600 mb-4">
        A radical new approach to building user interfaces with 
        less code and better performance.
      </p>
      <a href="https://svelte.dev" target="_blank" rel="noopener noreferrer" class="text-primary-600 hover:underline">
        Learn more →
      </a>
    </div>
    
    <div class="bg-white p-6 rounded-lg shadow-md">
      <h2 class="text-xl font-semibold text-primary-600 mb-3">FastAPI</h2>
      <p class="text-gray-600 mb-4">
        A modern, fast web framework for building APIs with Python 
        based on standard type hints.
      </p>
      <a href="https://fastapi.tiangolo.com" target="_blank" rel="noopener noreferrer" class="text-primary-600 hover:underline">
        Learn more →
      </a>
    </div>
    
    <div class="bg-white p-6 rounded-lg shadow-md">
      <h2 class="text-xl font-semibold text-primary-600 mb-3">Tailwind CSS</h2>
      <p class="text-gray-600 mb-4">
        A utility-first CSS framework for rapidly building custom 
        user interfaces without leaving your HTML.
      </p>
      <a href="https://tailwindcss.com" target="_blank" rel="noopener noreferrer" class="text-primary-600 hover:underline">
        Learn more →
      </a>
    </div>
  </div>
  
  <div class="mt-12 text-center">
    <Link to="/items" class="btn btn-primary">
      View Example Items
    </Link>
  </div>
</div> 