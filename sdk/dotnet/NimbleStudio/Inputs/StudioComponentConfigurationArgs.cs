// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.NimbleStudio.Inputs
{

    /// <summary>
    /// &lt;p&gt;The configuration of the studio component, based on component type.&lt;/p&gt;
    /// </summary>
    public sealed class StudioComponentConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("activeDirectoryConfiguration")]
        public Input<Inputs.StudioComponentActiveDirectoryConfigurationArgs>? ActiveDirectoryConfiguration { get; set; }

        [Input("computeFarmConfiguration")]
        public Input<Inputs.StudioComponentComputeFarmConfigurationArgs>? ComputeFarmConfiguration { get; set; }

        [Input("licenseServiceConfiguration")]
        public Input<Inputs.StudioComponentLicenseServiceConfigurationArgs>? LicenseServiceConfiguration { get; set; }

        [Input("sharedFileSystemConfiguration")]
        public Input<Inputs.StudioComponentSharedFileSystemConfigurationArgs>? SharedFileSystemConfiguration { get; set; }

        public StudioComponentConfigurationArgs()
        {
        }
        public static new StudioComponentConfigurationArgs Empty => new StudioComponentConfigurationArgs();
    }
}
