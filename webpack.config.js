const path = require('path');

module.exports = {
    entry: './frontend/app.js',
    output: {
        path: path.resolve(__dirname, 'static', 'js'),
        filename: 'bundle.js'
    },
    module: {
        rules: [
            {
                test: /\.svelte$/,
                exclude: /node_modules/,
                use: 'svelte-loader'
            },
            {
                test: /\.s[ac]ss$/i,
                use: [
                    'style-loader',
                    'css-loader',
                    'sass-loader',
                ]
            }
        ]
    }
};
