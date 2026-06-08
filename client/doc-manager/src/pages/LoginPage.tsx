import {
  Box,
  Button,
  Container,
  Paper,
  TextField,
  Typography,
  Alert,
} from "@mui/material";
import { useState } from "react";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import "./LoginPage.css";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setError("");
    setLoading(true);
    try {
      console.log("Login with", email, password);
    } catch {
      setError("Invalid email or password. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box className="login-root">
      <Container maxWidth="xs">
        <Paper elevation={4} className="login-paper">
          <Box className="login-icon-wrapper">
            <LockOutlinedIcon className="login-icon" />
          </Box>

          <Typography variant="h5" component="h1" align="center" fontWeight={700}>
            Document Manager
          </Typography>

          <Typography
            variant="body2"
            align="center"
            color="text.secondary"
            sx={{ mt: 1, mb: 3 }}
          >
            Sign in to manage your files
          </Typography>

          {error && (
            <Alert severity="error" sx={{ mb: 2 }}>
              {error}
            </Alert>
          )}

          <Box component="form" onSubmit={handleSubmit} sx={{ width: "100%" }}>
            <TextField
              label="Email"
              type="email"
              fullWidth
              margin="normal"
              required
              autoFocus
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
            <TextField
              label="Password"
              type="password"
              fullWidth
              margin="normal"
              required
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <Button
              type="submit"
              variant="contained"
              fullWidth
              size="large"
              sx={{ mt: 3, mb: 1, borderRadius: 2, backgroundColor: "#1a2b4a", "&:hover": { backgroundColor: "#0066cc" } }}
              disabled={loading}
            >
              {loading ? "Signing in..." : "Sign In"}
            </Button>
          </Box>
        </Paper>
      </Container>
    </Box>
  );
}
