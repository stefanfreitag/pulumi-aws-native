// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EMR
{
    /// <summary>
    /// Resource schema for AWS::EMR::Studio
    /// </summary>
    [AwsNativeResourceType("aws-native:emr:Studio")]
    public partial class Studio : Pulumi.CustomResource
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the EMR Studio.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// Specifies whether the Studio authenticates users using single sign-on (SSO) or IAM. Amazon EMR Studio currently only supports SSO authentication.
        /// </summary>
        [Output("authMode")]
        public Output<Pulumi.AwsNative.EMR.StudioAuthMode> AuthMode { get; private set; } = null!;

        /// <summary>
        /// The default Amazon S3 location to back up EMR Studio Workspaces and notebook files. A Studio user can select an alternative Amazon S3 location when creating a Workspace.
        /// </summary>
        [Output("defaultS3Location")]
        public Output<string> DefaultS3Location { get; private set; } = null!;

        /// <summary>
        /// A detailed description of the Studio.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The ID of the Amazon EMR Studio Engine security group. The Engine security group allows inbound network traffic from the Workspace security group, and it must be in the same VPC specified by VpcId.
        /// </summary>
        [Output("engineSecurityGroupId")]
        public Output<string> EngineSecurityGroupId { get; private set; } = null!;

        /// <summary>
        /// Your identity provider's authentication endpoint. Amazon EMR Studio redirects federated users to this endpoint for authentication when logging in to a Studio with the Studio URL.
        /// </summary>
        [Output("idpAuthUrl")]
        public Output<string?> IdpAuthUrl { get; private set; } = null!;

        /// <summary>
        /// The name of relay state parameter for external Identity Provider.
        /// </summary>
        [Output("idpRelayStateParameterName")]
        public Output<string?> IdpRelayStateParameterName { get; private set; } = null!;

        /// <summary>
        /// A descriptive name for the Amazon EMR Studio.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The IAM role that will be assumed by the Amazon EMR Studio. The service role provides a way for Amazon EMR Studio to interoperate with other AWS services.
        /// </summary>
        [Output("serviceRole")]
        public Output<string> ServiceRole { get; private set; } = null!;

        /// <summary>
        /// The ID of the EMR Studio.
        /// </summary>
        [Output("studioId")]
        public Output<string> StudioId { get; private set; } = null!;

        /// <summary>
        /// A list of up to 5 subnet IDs to associate with the Studio. The subnets must belong to the VPC specified by VpcId. Studio users can create a Workspace in any of the specified subnets.
        /// </summary>
        [Output("subnetIds")]
        public Output<ImmutableArray<string>> SubnetIds { get; private set; } = null!;

        /// <summary>
        /// A list of tags to associate with the Studio. Tags are user-defined key-value pairs that consist of a required key string with a maximum of 128 characters, and an optional value string with a maximum of 256 characters.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.StudioTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The unique Studio access URL.
        /// </summary>
        [Output("url")]
        public Output<string> Url { get; private set; } = null!;

        /// <summary>
        /// The IAM user role that will be assumed by users and groups logged in to a Studio. The permissions attached to this IAM role can be scoped down for each user or group using session policies.
        /// </summary>
        [Output("userRole")]
        public Output<string?> UserRole { get; private set; } = null!;

        /// <summary>
        /// The ID of the Amazon Virtual Private Cloud (Amazon VPC) to associate with the Studio.
        /// </summary>
        [Output("vpcId")]
        public Output<string> VpcId { get; private set; } = null!;

        /// <summary>
        /// The ID of the Amazon EMR Studio Workspace security group. The Workspace security group allows outbound network traffic to resources in the Engine security group, and it must be in the same VPC specified by VpcId.
        /// </summary>
        [Output("workspaceSecurityGroupId")]
        public Output<string> WorkspaceSecurityGroupId { get; private set; } = null!;


        /// <summary>
        /// Create a Studio resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Studio(string name, StudioArgs args, CustomResourceOptions? options = null)
            : base("aws-native:emr:Studio", name, args ?? new StudioArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Studio(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:emr:Studio", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Studio resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Studio Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Studio(name, id, options);
        }
    }

    public sealed class StudioArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specifies whether the Studio authenticates users using single sign-on (SSO) or IAM. Amazon EMR Studio currently only supports SSO authentication.
        /// </summary>
        [Input("authMode", required: true)]
        public Input<Pulumi.AwsNative.EMR.StudioAuthMode> AuthMode { get; set; } = null!;

        /// <summary>
        /// The default Amazon S3 location to back up EMR Studio Workspaces and notebook files. A Studio user can select an alternative Amazon S3 location when creating a Workspace.
        /// </summary>
        [Input("defaultS3Location", required: true)]
        public Input<string> DefaultS3Location { get; set; } = null!;

        /// <summary>
        /// A detailed description of the Studio.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The ID of the Amazon EMR Studio Engine security group. The Engine security group allows inbound network traffic from the Workspace security group, and it must be in the same VPC specified by VpcId.
        /// </summary>
        [Input("engineSecurityGroupId", required: true)]
        public Input<string> EngineSecurityGroupId { get; set; } = null!;

        /// <summary>
        /// Your identity provider's authentication endpoint. Amazon EMR Studio redirects federated users to this endpoint for authentication when logging in to a Studio with the Studio URL.
        /// </summary>
        [Input("idpAuthUrl")]
        public Input<string>? IdpAuthUrl { get; set; }

        /// <summary>
        /// The name of relay state parameter for external Identity Provider.
        /// </summary>
        [Input("idpRelayStateParameterName")]
        public Input<string>? IdpRelayStateParameterName { get; set; }

        /// <summary>
        /// A descriptive name for the Amazon EMR Studio.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// The IAM role that will be assumed by the Amazon EMR Studio. The service role provides a way for Amazon EMR Studio to interoperate with other AWS services.
        /// </summary>
        [Input("serviceRole", required: true)]
        public Input<string> ServiceRole { get; set; } = null!;

        [Input("subnetIds", required: true)]
        private InputList<string>? _subnetIds;

        /// <summary>
        /// A list of up to 5 subnet IDs to associate with the Studio. The subnets must belong to the VPC specified by VpcId. Studio users can create a Workspace in any of the specified subnets.
        /// </summary>
        public InputList<string> SubnetIds
        {
            get => _subnetIds ?? (_subnetIds = new InputList<string>());
            set => _subnetIds = value;
        }

        [Input("tags")]
        private InputList<Inputs.StudioTagArgs>? _tags;

        /// <summary>
        /// A list of tags to associate with the Studio. Tags are user-defined key-value pairs that consist of a required key string with a maximum of 128 characters, and an optional value string with a maximum of 256 characters.
        /// </summary>
        public InputList<Inputs.StudioTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.StudioTagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// The IAM user role that will be assumed by users and groups logged in to a Studio. The permissions attached to this IAM role can be scoped down for each user or group using session policies.
        /// </summary>
        [Input("userRole")]
        public Input<string>? UserRole { get; set; }

        /// <summary>
        /// The ID of the Amazon Virtual Private Cloud (Amazon VPC) to associate with the Studio.
        /// </summary>
        [Input("vpcId", required: true)]
        public Input<string> VpcId { get; set; } = null!;

        /// <summary>
        /// The ID of the Amazon EMR Studio Workspace security group. The Workspace security group allows outbound network traffic to resources in the Engine security group, and it must be in the same VPC specified by VpcId.
        /// </summary>
        [Input("workspaceSecurityGroupId", required: true)]
        public Input<string> WorkspaceSecurityGroupId { get; set; } = null!;

        public StudioArgs()
        {
        }
    }
}
