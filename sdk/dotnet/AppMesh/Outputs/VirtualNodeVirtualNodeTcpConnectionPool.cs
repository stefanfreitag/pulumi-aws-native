// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppMesh.Outputs
{

    [OutputType]
    public sealed class VirtualNodeVirtualNodeTcpConnectionPool
    {
        public readonly int MaxConnections;

        [OutputConstructor]
        private VirtualNodeVirtualNodeTcpConnectionPool(int maxConnections)
        {
            MaxConnections = maxConnections;
        }
    }
}
