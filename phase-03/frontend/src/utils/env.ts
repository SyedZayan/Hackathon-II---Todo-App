import { createEnv } from "@t3-oss/env-nextjs";
import { z } from "zod";

export const env = createEnv({
  server: {
    // Node
    NODE_ENV: z.enum(["development", "test", "production"]).default("development"),

    // Better Auth
    BETTER_AUTH_URL: z.string().default("http://localhost:3000"),
    BETTER_AUTH_SECRET: z.string(),

    // Database
    DATABASE_URL: z.string(),

    // SMTP / Email
    SMTP_HOST: z.string().default("smtp.gmail.com"),
    SMTP_USER: z.string(),
    SMTP_PASS: z.string(),

    // DB timeouts (ENV VARS ARE STRINGS → MUST COERCE)
    DB_IDLE_TIMEOUT: z.coerce.number().default(30000),
    DB_CONNECT_TIMEOUT: z.coerce.number().default(2000),
    DB_QUERY_TIMEOUT: z.coerce.number().default(60000),
  },

  client: {
    NEXT_PUBLIC_BASE_URL: z.string(),
    NEXT_PUBLIC_API_BASE_URL: z.string(),
    NEXT_PUBLIC_CHATKIT_DOMAIN_KEY: z.string(),
  },

  runtimeEnv: {
    // Node
    NODE_ENV: process.env.NODE_ENV,

    // Client
    NEXT_PUBLIC_BASE_URL: process.env.NEXT_PUBLIC_BASE_URL,
    NEXT_PUBLIC_API_BASE_URL: process.env.NEXT_PUBLIC_API_BASE_URL,
    NEXT_PUBLIC_CHATKIT_DOMAIN_KEY: process.env.NEXT_PUBLIC_CHATKIT_DOMAIN_KEY,

    // Server
    BETTER_AUTH_URL: process.env.BETTER_AUTH_URL,
    BETTER_AUTH_SECRET: process.env.BETTER_AUTH_SECRET,
    DATABASE_URL: process.env.DATABASE_URL,

    SMTP_HOST: process.env.SMTP_HOST,
    SMTP_USER: process.env.SMTP_USER,
    SMTP_PASS: process.env.SMTP_PASS,

    DB_IDLE_TIMEOUT: process.env.DB_IDLE_TIMEOUT,
    DB_CONNECT_TIMEOUT: process.env.DB_CONNECT_TIMEOUT,
    DB_QUERY_TIMEOUT: process.env.DB_QUERY_TIMEOUT,
  },
});
