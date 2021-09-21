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
    public sealed class VirtualServiceVirtualServiceProvider
    {
        public readonly Outputs.VirtualServiceVirtualNodeServiceProvider? VirtualNode;
        public readonly Outputs.VirtualServiceVirtualRouterServiceProvider? VirtualRouter;

        [OutputConstructor]
        private VirtualServiceVirtualServiceProvider(
            Outputs.VirtualServiceVirtualNodeServiceProvider? virtualNode,

            Outputs.VirtualServiceVirtualRouterServiceProvider? virtualRouter)
        {
            VirtualNode = virtualNode;
            VirtualRouter = virtualRouter;
        }
    }
}
