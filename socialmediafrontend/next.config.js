/** @type {import('next').NextConfig} */
//next.config.js
module.exports = {
    reactStrictMode: true,
    webp: {
        preset: "default",
        quality: 100,
    },
    images: {
        domains: ["randomuser.me", "firebasestorage.googleapis.com"],
    },
    //Internationalization
    i18n: {
        locales: ["en", "it"],
        defaultLocale: "en",
    },
};