<script lang="ts">
  import { Link } from 'svelte-navigator';
</script>

<nav class="bg-white shadow">
  <div class="container-narrow py-4">
    <div class="flex justify-between items-center">
      <div class="flex items-center">
        <Link to="/" class="text-xl font-bold text-primary-600">
          Svelte + FastAPI
        </Link>
      </div>
      
      <div class="flex space-x-6">
        <Link to="/" class="text-gray-700 hover:text-primary-600">Home</Link>
        <Link to="/items" class="text-gray-700 hover:text-primary-600">Items</Link>
        <Link to="/about" class="text-gray-700 hover:text-primary-600">About</Link>
      </div>
    </div>
  </div>
</nav> 