// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaLive.Inputs
{

    /// <summary>
    /// Multiplex Program settings configuration.
    /// </summary>
    public sealed class MultiplexprogramMultiplexProgramSettingsArgs : global::Pulumi.ResourceArgs
    {
        [Input("preferredChannelPipeline")]
        public Input<Pulumi.AwsNative.MediaLive.MultiplexprogramPreferredChannelPipeline>? PreferredChannelPipeline { get; set; }

        /// <summary>
        /// Unique program number.
        /// </summary>
        [Input("programNumber", required: true)]
        public Input<int> ProgramNumber { get; set; } = null!;

        /// <summary>
        /// Transport stream service descriptor configuration for the Multiplex program.
        /// </summary>
        [Input("serviceDescriptor")]
        public Input<Inputs.MultiplexprogramMultiplexProgramServiceDescriptorArgs>? ServiceDescriptor { get; set; }

        /// <summary>
        /// Program video settings configuration.
        /// </summary>
        [Input("videoSettings")]
        public Input<Inputs.MultiplexprogramMultiplexVideoSettingsArgs>? VideoSettings { get; set; }

        public MultiplexprogramMultiplexProgramSettingsArgs()
        {
        }
        public static new MultiplexprogramMultiplexProgramSettingsArgs Empty => new MultiplexprogramMultiplexProgramSettingsArgs();
    }
}
