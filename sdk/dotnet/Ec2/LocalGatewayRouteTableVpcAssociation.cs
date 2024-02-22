// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2
{
    /// <summary>
    /// Describes an association between a local gateway route table and a VPC.
    /// </summary>
    [AwsNativeResourceType("aws-native:ec2:LocalGatewayRouteTableVpcAssociation")]
    public partial class LocalGatewayRouteTableVpcAssociation : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The ID of the local gateway.
        /// </summary>
        [Output("localGatewayId")]
        public Output<string> LocalGatewayId { get; private set; } = null!;

        /// <summary>
        /// The ID of the local gateway route table.
        /// </summary>
        [Output("localGatewayRouteTableId")]
        public Output<string> LocalGatewayRouteTableId { get; private set; } = null!;

        /// <summary>
        /// The ID of the association.
        /// </summary>
        [Output("localGatewayRouteTableVpcAssociationId")]
        public Output<string> LocalGatewayRouteTableVpcAssociationId { get; private set; } = null!;

        /// <summary>
        /// The state of the association.
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        /// <summary>
        /// The tags for the association.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The ID of the VPC.
        /// </summary>
        [Output("vpcId")]
        public Output<string> VpcId { get; private set; } = null!;


        /// <summary>
        /// Create a LocalGatewayRouteTableVpcAssociation resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public LocalGatewayRouteTableVpcAssociation(string name, LocalGatewayRouteTableVpcAssociationArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ec2:LocalGatewayRouteTableVpcAssociation", name, args ?? new LocalGatewayRouteTableVpcAssociationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private LocalGatewayRouteTableVpcAssociation(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ec2:LocalGatewayRouteTableVpcAssociation", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "localGatewayRouteTableId",
                    "vpcId",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing LocalGatewayRouteTableVpcAssociation resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static LocalGatewayRouteTableVpcAssociation Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new LocalGatewayRouteTableVpcAssociation(name, id, options);
        }
    }

    public sealed class LocalGatewayRouteTableVpcAssociationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the local gateway route table.
        /// </summary>
        [Input("localGatewayRouteTableId", required: true)]
        public Input<string> LocalGatewayRouteTableId { get; set; } = null!;

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// The tags for the association.
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// The ID of the VPC.
        /// </summary>
        [Input("vpcId", required: true)]
        public Input<string> VpcId { get; set; } = null!;

        public LocalGatewayRouteTableVpcAssociationArgs()
        {
        }
        public static new LocalGatewayRouteTableVpcAssociationArgs Empty => new LocalGatewayRouteTableVpcAssociationArgs();
    }
}
