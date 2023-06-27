// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ImageBuilder.Inputs
{

    /// <summary>
    /// Image tests configuration.
    /// </summary>
    public sealed class ImagePipelineImageTestsConfigurationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Defines if tests should be executed when building this image.
        /// </summary>
        [Input("imageTestsEnabled")]
        public Input<bool>? ImageTestsEnabled { get; set; }

        /// <summary>
        /// The maximum time in minutes that tests are permitted to run.
        /// </summary>
        [Input("timeoutMinutes")]
        public Input<int>? TimeoutMinutes { get; set; }

        public ImagePipelineImageTestsConfigurationArgs()
        {
        }
        public static new ImagePipelineImageTestsConfigurationArgs Empty => new ImagePipelineImageTestsConfigurationArgs();
    }
}
