<template>
  <div class="home">
      <home />
      <about />
      <download />
      <pricing />
      <contact />
  </div>
</template>

<script>
import home from "../components/HomeSection";
import about from "../components/AboutSection";
import download from "../components/DownloadSection";
import pricing from "../components/PricingSection";
import contact from "../components/ContactSection";

  export default {
    name: 'Home',

    components: {
      home,
      about,
      download,
      pricing,
      contact,
    },
  }
</script>
