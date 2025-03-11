<script lang="ts">
  import { onMount } from 'svelte';
  
  interface Item {
    id: number;
    name: string;
    description: string | null;
    price: number;
  }
  
  let items: Item[] = [];
  let loading = true;
  let error = '';
  
  // Form state
  let newItem = {
    name: '',
    description: '',
    price: 0
  };
  
  onMount(async () => {
    try {
      const response = await fetch('/api/v1/items');
      if (!response.ok) {
        throw new Error(`Error: ${response.status}`);
      }
      items = await response.json();
      loading = false;
    } catch (err) {
      console.error('Failed to fetch items:', err);
      error = 'Failed to load items. Please try again later.';
      loading = false;
    }
  });
  
  async function handleSubmit() {
    try {
      const response = await fetch('/api/v1/items', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(newItem)
      });
      
      if (!response.ok) {
        throw new Error(`Error: ${response.status}`);
      }
      
      const createdItem = await response.json();
      items = [...items, createdItem];
      
      // Reset form
      newItem = {
        name: '',
        description: '',
        price: 0
      };
      
    } catch (err) {
      console.error('Failed to create item:', err);
      error = 'Failed to create item. Please try again.';
    }
  }
  
  async function deleteItem(id: number) {
    try {
      const response = await fetch(`/api/v1/items/${id}`, {
        method: 'DELETE'
      });
      
      if (!response.ok) {
        throw new Error(`Error: ${response.status}`);
      }
      
      // Remove item from list
      items = items.filter(item => item.id !== id);
      
    } catch (err) {
      console.error('Failed to delete item:', err);
      error = 'Failed to delete item. Please try again.';
    }
  }
</script>

<div>
  <h1 class="text-3xl font-bold mb-6">Items</h1>
  
  {#if error}
    <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-6">
      {error}
    </div>
  {/if}
  
  <div class="bg-white p-6 rounded-lg shadow-md mb-8">
    <h2 class="text-xl font-semibold mb-4">Add New Item</h2>
    
    <form on:submit|preventDefault={handleSubmit} class="space-y-4">
      <div>
        <label for="name" class="block text-sm font-medium text-gray-700 mb-1">Name</label>
        <input
          type="text"
          id="name"
          bind:value={newItem.name}
          required
          class="w-full px-3 py-2 border border-gray-300 rounded-md"
        />
      </div>
      
      <div>
        <label for="description" class="block text-sm font-medium text-gray-700 mb-1">Description</label>
        <textarea
          id="description"
          bind:value={newItem.description}
          class="w-full px-3 py-2 border border-gray-300 rounded-md"
          rows="3"
        ></textarea>
      </div>
      
      <div>
        <label for="price" class="block text-sm font-medium text-gray-700 mb-1">Price</label>
        <input
          type="number"
          id="price"
          bind:value={newItem.price}
          min="0"
          step="0.01"
          required
          class="w-full px-3 py-2 border border-gray-300 rounded-md"
        />
      </div>
      
      <button type="submit" class="btn btn-primary">
        Add Item
      </button>
    </form>
  </div>
  
  <div class="bg-white p-6 rounded-lg shadow-md">
    <h2 class="text-xl font-semibold mb-4">Item List</h2>
    
    {#if loading}
      <p class="text-gray-600">Loading items...</p>
    {:else if items.length === 0}
      <p class="text-gray-600">No items found. Add your first item above!</p>
    {:else}
      <div class="overflow-x-auto">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">ID</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Description</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Price</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            {#each items as item (item.id)}
              <tr>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{item.id}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{item.name}</td>
                <td class="px-6 py-4 text-sm text-gray-500">{item.description || '-'}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">${item.price.toFixed(2)}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  <button 
                    on:click={() => deleteItem(item.id)}
                    class="text-red-600 hover:text-red-900"
                  >
                    Delete
                  </button>
                </td>
              </tr>
            {/each}
          </tbody>
        </table>
      </div>
    {/if}
  </div>
</div> 