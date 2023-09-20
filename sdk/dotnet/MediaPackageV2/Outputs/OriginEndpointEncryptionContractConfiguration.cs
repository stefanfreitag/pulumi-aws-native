// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaPackageV2.Outputs
{

    /// <summary>
    /// &lt;p&gt;Configure one or more content encryption keys for your endpoints that use SPEKE Version 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use.&lt;/p&gt;
    /// </summary>
    [OutputType]
    public sealed class OriginEndpointEncryptionContractConfiguration
    {
        public readonly Pulumi.AwsNative.MediaPackageV2.OriginEndpointPresetSpeke20Audio PresetSpeke20Audio;
        public readonly Pulumi.AwsNative.MediaPackageV2.OriginEndpointPresetSpeke20Video PresetSpeke20Video;

        [OutputConstructor]
        private OriginEndpointEncryptionContractConfiguration(
            Pulumi.AwsNative.MediaPackageV2.OriginEndpointPresetSpeke20Audio presetSpeke20Audio,

            Pulumi.AwsNative.MediaPackageV2.OriginEndpointPresetSpeke20Video presetSpeke20Video)
        {
            PresetSpeke20Audio = presetSpeke20Audio;
            PresetSpeke20Video = presetSpeke20Video;
        }
    }
}
