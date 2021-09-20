// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    /// <summary>
    /// &lt;p&gt;The theme configuration. This configuration contains all of the display properties for
    ///             a theme.&lt;/p&gt;
    /// </summary>
    public sealed class ThemeThemeConfigurationArgs : Pulumi.ResourceArgs
    {
        [Input("dataColorPalette")]
        public Input<Inputs.ThemeDataColorPaletteArgs>? DataColorPalette { get; set; }

        [Input("sheet")]
        public Input<Inputs.ThemeSheetStyleArgs>? Sheet { get; set; }

        [Input("typography")]
        public Input<Inputs.ThemeTypographyArgs>? Typography { get; set; }

        [Input("uIColorPalette")]
        public Input<Inputs.ThemeUIColorPaletteArgs>? UIColorPalette { get; set; }

        public ThemeThemeConfigurationArgs()
        {
        }
    }
}
