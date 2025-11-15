<template>
    <a
        :href="site.url"
        target="_blank"
        rel="noopener noreferrer"
        class="group relative flex flex-col items-center justify-center p-6 rounded-xl shadow-md hover:shadow-lg transition-all duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105 bg-gray-800 hover:bg-gray-700"
    >
        <!-- 角标 (右下角) -->
        <span
            v-if="site.badge"
            class="absolute bottom-0 right-0 px-3 py-1 text-white text-xs font-bold rounded-tl-xl"
            :class="site.color"
        >
            {{ site.badge.toUpperCase() }}
        </span>

        <!-- 图标容器 -->
        <div
            class="w-16 h-16 rounded-full flex items-center justify-center transition-colors duration-300"
            :class="site.color"
        >
            <!-- 内联 SVG 图标 -->
            <Icon class="w-8 h-8 text-white" :icon="site.icon"></Icon>
        </div>

        <!-- 网站标题 -->
        <h2 class="mt-4 text-lg font-semibold text-gray-100 text-center">
            {{ site.title }}
        </h2>
        <!-- 网站描述 -->
        <p class="mt-1 text-sm text-gray-400 text-center">
            {{ site.description }}
        </p>
    </a>
</template>

<script setup lang="ts">
import { Icon } from '@iconify/vue'

defineProps<{
    site: {
        title: string
        description: string
        url: string
        color: string
        icon: string
        badge?: string
    }
}>()
</script>

<style scoped></style>
