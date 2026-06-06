import { Box, Button, Container, Paper, TextField, Typography } from "@mui/material";
import { useNavigate } from "react-router-dom";

export default function LoginPage() {
  // const navigate = useNavigate();
  //
  // const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
  //   event.preventDefault();
  //   navigate("/files");
  // };

  return (
    <Container maxWidth="sm">
      <Box sx={{ minHeight: "100vh", display: "flex", alignItems: "center", justifyContent: "center" }}>
        <Paper elevation={3} sx={{ width: "100%", p: 4, borderRadius: 3 }}>
          <Typography variant="h4" component="h1" gutterBottom>
            Document Manager
          </Typography>

          <Typography variant="body2" color="text.secondary" sx={{ mb: 3 }}>
            Sign in to upload, version, and manage your files.
          </Typography>

          <Box component="form">
            <TextField label="Email" type="email" fullWidth margin="normal" required />
            <TextField label="Password" type="password" fullWidth margin="normal" required />
            <Button type="submit" variant="contained" fullWidth size="large" sx={{ mt: 3 }}>
              Log In
            </Button>
          </Box>
        </Paper>
      </Box>
    </Container>
  );
}
