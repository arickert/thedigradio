import { defineConfig } from "tinacms";

// Your hosting provider likely exposes this as an environment variable
const branch = process.env.HEAD || process.env.VERCEL_GIT_COMMIT_REF || "master";

export default defineConfig({
  branch,
  clientId: process.env.TINA_PUBLIC_CLIENT_ID, 
  token: process.env.TINA_TOKEN,

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
            list:true,
            label: "Categories",
          },
          {
            type: "string",
            name: "tags",
            list:true,
            label: "Tags",
          },
          {
            type: "number",
            name: "post_id",
            label: "PostID",
          },
          {
            type: "string",
            name: "googlelink",
            label: "Google Link",
          },
          {
            type: "string",
            name: "spotifylink",
            label: "Spotify Link",
          },
          {
            type: "string",
            name: "applelink",
            label: "Apple Link",
          },
          
        ],
      },
    ],
  },
});
