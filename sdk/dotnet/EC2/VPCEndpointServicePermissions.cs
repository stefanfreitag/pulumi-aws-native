// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2
{
    /// <summary>
    /// Resource Type definition for AWS::EC2::VPCEndpointServicePermissions
    /// </summary>
    [Obsolete(@"VPCEndpointServicePermissions is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:ec2:VPCEndpointServicePermissions")]
    public partial class VPCEndpointServicePermissions : global::Pulumi.CustomResource
    {
        [Output("allowedPrincipals")]
        public Output<ImmutableArray<string>> AllowedPrincipals { get; private set; } = null!;

        [Output("serviceId")]
        public Output<string> ServiceId { get; private set; } = null!;


        /// <summary>
        /// Create a VPCEndpointServicePermissions resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public VPCEndpointServicePermissions(string name, VPCEndpointServicePermissionsArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ec2:VPCEndpointServicePermissions", name, args ?? new VPCEndpointServicePermissionsArgs(), MakeResourceOptions(options, ""))
        {
        }

        private VPCEndpointServicePermissions(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ec2:VPCEndpointServicePermissions", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing VPCEndpointServicePermissions resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static VPCEndpointServicePermissions Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new VPCEndpointServicePermissions(name, id, options);
        }
    }

    public sealed class VPCEndpointServicePermissionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("allowedPrincipals")]
        private InputList<string>? _allowedPrincipals;
        public InputList<string> AllowedPrincipals
        {
            get => _allowedPrincipals ?? (_allowedPrincipals = new InputList<string>());
            set => _allowedPrincipals = value;
        }

        [Input("serviceId", required: true)]
        public Input<string> ServiceId { get; set; } = null!;

        public VPCEndpointServicePermissionsArgs()
        {
        }
        public static new VPCEndpointServicePermissionsArgs Empty => new VPCEndpointServicePermissionsArgs();
    }
}
