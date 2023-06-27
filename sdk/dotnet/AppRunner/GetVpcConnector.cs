// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppRunner
{
    public static class GetVpcConnector
    {
        /// <summary>
        /// The AWS::AppRunner::VpcConnector resource specifies an App Runner VpcConnector.
        /// </summary>
        public static Task<GetVpcConnectorResult> InvokeAsync(GetVpcConnectorArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetVpcConnectorResult>("aws-native:apprunner:getVpcConnector", args ?? new GetVpcConnectorArgs(), options.WithDefaults());

        /// <summary>
        /// The AWS::AppRunner::VpcConnector resource specifies an App Runner VpcConnector.
        /// </summary>
        public static Output<GetVpcConnectorResult> Invoke(GetVpcConnectorInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetVpcConnectorResult>("aws-native:apprunner:getVpcConnector", args ?? new GetVpcConnectorInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetVpcConnectorArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of this VPC connector.
        /// </summary>
        [Input("vpcConnectorArn", required: true)]
        public string VpcConnectorArn { get; set; } = null!;

        public GetVpcConnectorArgs()
        {
        }
        public static new GetVpcConnectorArgs Empty => new GetVpcConnectorArgs();
    }

    public sealed class GetVpcConnectorInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of this VPC connector.
        /// </summary>
        [Input("vpcConnectorArn", required: true)]
        public Input<string> VpcConnectorArn { get; set; } = null!;

        public GetVpcConnectorInvokeArgs()
        {
        }
        public static new GetVpcConnectorInvokeArgs Empty => new GetVpcConnectorInvokeArgs();
    }


    [OutputType]
    public sealed class GetVpcConnectorResult
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of this VPC connector.
        /// </summary>
        public readonly string? VpcConnectorArn;
        /// <summary>
        /// The revision of this VPC connector. It's unique among all the active connectors ("Status": "ACTIVE") that share the same Name.
        /// </summary>
        public readonly int? VpcConnectorRevision;

        [OutputConstructor]
        private GetVpcConnectorResult(
            string? vpcConnectorArn,

            int? vpcConnectorRevision)
        {
            VpcConnectorArn = vpcConnectorArn;
            VpcConnectorRevision = vpcConnectorRevision;
        }
    }
}
