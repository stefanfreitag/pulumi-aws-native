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
    /// &lt;p&gt;The configuration for a render farm that is associated with a studio resource.&lt;/p&gt;
    /// </summary>
    public sealed class StudioComponentComputeFarmConfigurationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// &lt;p&gt;The name of an Active Directory user that is used on ComputeFarm worker instances.&lt;/p&gt;
        /// </summary>
        [Input("activeDirectoryUser")]
        public Input<string>? ActiveDirectoryUser { get; set; }

        /// <summary>
        /// &lt;p&gt;The endpoint of the ComputeFarm that is accessed by the studio component resource.&lt;/p&gt;
        /// </summary>
        [Input("endpoint")]
        public Input<string>? Endpoint { get; set; }

        public StudioComponentComputeFarmConfigurationArgs()
        {
        }
        public static new StudioComponentComputeFarmConfigurationArgs Empty => new StudioComponentComputeFarmConfigurationArgs();
    }
}
