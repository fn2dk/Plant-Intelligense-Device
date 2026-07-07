import type { Metadata } from "next";
import "./styles.css";

export const metadata: Metadata = {
  title: "Plant Intelligense Device",
  description: "Engineering diagram intelligence platform"
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="da">
      <body>{children}</body>
    </html>
  );
}
