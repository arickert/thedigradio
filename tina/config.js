import { defineConfig } from "tinacms";

// Your hosting provider likely exposes this as an environment variable
const branch = process.env.HEAD || process.env.VERCEL_GIT_COMMIT_REF || "master";

export default defineConfig({
  branch,
  clientId: "9c28524f-cd54-4cb7-b7f6-3cc0fcda37d3", // Get this from tina.io
  token: "247d3c3a1c3e00bb1e2539a13763c6037692b7ee", // Get this from tina.io

  build: {
    outputFolder: "admin",
    publicFolder: "./",
  },
  media: {
    tina: {
      mediaRoot: "",
      publicFolder: "./",
    },
  },
  schema: {
    collections: [
      {
        name: "post",
        label: "Posts",
        path: "_posts",
        fields: [
          {
            type: "string",
            name: "title",
            label: "Title",
            isTitle: true,
            required: true,
          },
          {
            type: "rich-text",
            name: "body",
            label: "Body",
            isBody: true,
          },
          {
            type: "string",
            name: "permalink",
            label: "Permalink",
          },
                    {
            type: "string",
            name: "audiolink",
            label: "Audiolink",
          },
          {
            type: "string",
            name: "categories",
            list:'true',
            label: "Categories",
          },
          {
            type: "string",
            name: "tags",
            list:'true',
            label: "Tags",
          },
          {
            type: "number",
            name: "post_id",
            label: "PostID",
          },
        ],
      },
    ],
  },
});
