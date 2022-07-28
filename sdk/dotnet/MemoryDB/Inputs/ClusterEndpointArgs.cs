// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MemoryDB.Inputs
{

    public sealed class ClusterEndpointArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The DNS address of the primary read-write node.
        /// </summary>
        [Input("address")]
        public Input<string>? Address { get; set; }

        /// <summary>
        /// The port number that the engine is listening on. 
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        public ClusterEndpointArgs()
        {
        }
        public static new ClusterEndpointArgs Empty => new ClusterEndpointArgs();
    }
}
