<template>
    <div
        class="fixed inset-0 flex flex-col bg-gradient-to-br from-gray-900 to-slate-800"
    >
        <header
            class="h-[140px] text-white flex flex-col items-center justify-center shrink-0"
        >
            <h1 class="text-4xl font-boldtext-gray-100">{{ config.title }}</h1>
            <p class="mt-2 text-lg text-gray-400">{{ config.description }}</p>
        </header>

        <main class="flex-1 min-h-[calc(100%-200px)] overflow-auto">
            <div
                class="max-w-6xl mx-auto py-4 px-4 grid grid-cols-2 md:grid-cols-4 gap-6"
            >
                <Card
                    v-for="(site, index) in config.sites"
                    :key="index"
                    :site="site"
                ></Card>
            </div>
        </main>

        <footer
            class="h-[60px] text-gray-400 text-sm flex items-center justify-center shrink-0"
        >
            <p>
                {{ config.copyright }}
            </p>
        </footer>
    </div>
</template>

<script setup lang="ts">
import Card from './components/Card.vue'
import config from './config.json'
</script>
