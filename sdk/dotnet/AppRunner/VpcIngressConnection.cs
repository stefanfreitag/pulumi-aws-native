// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppRunner
{
    /// <summary>
    /// The AWS::AppRunner::VpcIngressConnection resource is an App Runner resource that specifies an App Runner VpcIngressConnection.
    /// </summary>
    [AwsNativeResourceType("aws-native:apprunner:VpcIngressConnection")]
    public partial class VpcIngressConnection : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The Domain name associated with the VPC Ingress Connection.
        /// </summary>
        [Output("domainName")]
        public Output<string> DomainName { get; private set; } = null!;

        [Output("ingressVpcConfiguration")]
        public Output<Outputs.VpcIngressConnectionIngressVpcConfiguration> IngressVpcConfiguration { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the service.
        /// </summary>
        [Output("serviceArn")]
        public Output<string> ServiceArn { get; private set; } = null!;

        /// <summary>
        /// The current status of the VpcIngressConnection.
        /// </summary>
        [Output("status")]
        public Output<Pulumi.AwsNative.AppRunner.VpcIngressConnectionStatus> Status { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.CreateOnlyTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the VpcIngressConnection.
        /// </summary>
        [Output("vpcIngressConnectionArn")]
        public Output<string> VpcIngressConnectionArn { get; private set; } = null!;

        /// <summary>
        /// The customer-provided Vpc Ingress Connection name.
        /// </summary>
        [Output("vpcIngressConnectionName")]
        public Output<string?> VpcIngressConnectionName { get; private set; } = null!;


        /// <summary>
        /// Create a VpcIngressConnection resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public VpcIngressConnection(string name, VpcIngressConnectionArgs args, CustomResourceOptions? options = null)
            : base("aws-native:apprunner:VpcIngressConnection", name, args ?? new VpcIngressConnectionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private VpcIngressConnection(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:apprunner:VpcIngressConnection", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "serviceArn",
                    "tags[*]",
                    "vpcIngressConnectionName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing VpcIngressConnection resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static VpcIngressConnection Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new VpcIngressConnection(name, id, options);
        }
    }

    public sealed class VpcIngressConnectionArgs : global::Pulumi.ResourceArgs
    {
        [Input("ingressVpcConfiguration", required: true)]
        public Input<Inputs.VpcIngressConnectionIngressVpcConfigurationArgs> IngressVpcConfiguration { get; set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the service.
        /// </summary>
        [Input("serviceArn", required: true)]
        public Input<string> ServiceArn { get; set; } = null!;

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.CreateOnlyTagArgs>? _tags;
        public InputList<Pulumi.AwsNative.Inputs.CreateOnlyTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.CreateOnlyTagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// The customer-provided Vpc Ingress Connection name.
        /// </summary>
        [Input("vpcIngressConnectionName")]
        public Input<string>? VpcIngressConnectionName { get; set; }

        public VpcIngressConnectionArgs()
        {
        }
        public static new VpcIngressConnectionArgs Empty => new VpcIngressConnectionArgs();
    }
}
