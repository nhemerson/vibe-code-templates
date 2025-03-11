<script lang="ts">
  import { Router, Route } from 'svelte-navigator';
  import Navbar from './lib/components/Navbar.svelte';
  import Footer from './lib/components/Footer.svelte';
  import Home from './routes/Home.svelte';
  import Items from './routes/Items.svelte';
  import About from './routes/About.svelte';
</script>

<Router>
  <div class="flex flex-col min-h-screen">
    <Navbar />
    
    <main class="flex-grow">
      <div class="container-narrow py-8">
        <Route path="/" component={Home} />
        <Route path="/items" component={Items} />
        <Route path="/about" component={About} />
      </div>
    </main>
    
    <Footer />
  </div>
</Router> 