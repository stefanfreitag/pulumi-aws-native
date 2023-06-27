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
    /// Resource Type definition for AWS::EC2::EC2Fleet
    /// </summary>
    [AwsNativeResourceType("aws-native:ec2:EC2Fleet")]
    public partial class EC2Fleet : global::Pulumi.CustomResource
    {
        [Output("context")]
        public Output<string?> Context { get; private set; } = null!;

        [Output("excessCapacityTerminationPolicy")]
        public Output<Pulumi.AwsNative.EC2.EC2FleetExcessCapacityTerminationPolicy?> ExcessCapacityTerminationPolicy { get; private set; } = null!;

        [Output("fleetId")]
        public Output<string> FleetId { get; private set; } = null!;

        [Output("launchTemplateConfigs")]
        public Output<ImmutableArray<Outputs.EC2FleetFleetLaunchTemplateConfigRequest>> LaunchTemplateConfigs { get; private set; } = null!;

        [Output("onDemandOptions")]
        public Output<Outputs.EC2FleetOnDemandOptionsRequest?> OnDemandOptions { get; private set; } = null!;

        [Output("replaceUnhealthyInstances")]
        public Output<bool?> ReplaceUnhealthyInstances { get; private set; } = null!;

        [Output("spotOptions")]
        public Output<Outputs.EC2FleetSpotOptionsRequest?> SpotOptions { get; private set; } = null!;

        [Output("tagSpecifications")]
        public Output<ImmutableArray<Outputs.EC2FleetTagSpecification>> TagSpecifications { get; private set; } = null!;

        [Output("targetCapacitySpecification")]
        public Output<Outputs.EC2FleetTargetCapacitySpecificationRequest> TargetCapacitySpecification { get; private set; } = null!;

        [Output("terminateInstancesWithExpiration")]
        public Output<bool?> TerminateInstancesWithExpiration { get; private set; } = null!;

        [Output("type")]
        public Output<Pulumi.AwsNative.EC2.EC2FleetType?> Type { get; private set; } = null!;

        [Output("validFrom")]
        public Output<string?> ValidFrom { get; private set; } = null!;

        [Output("validUntil")]
        public Output<string?> ValidUntil { get; private set; } = null!;


        /// <summary>
        /// Create a EC2Fleet resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public EC2Fleet(string name, EC2FleetArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ec2:EC2Fleet", name, args ?? new EC2FleetArgs(), MakeResourceOptions(options, ""))
        {
        }

        private EC2Fleet(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ec2:EC2Fleet", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing EC2Fleet resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static EC2Fleet Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new EC2Fleet(name, id, options);
        }
    }

    public sealed class EC2FleetArgs : global::Pulumi.ResourceArgs
    {
        [Input("context")]
        public Input<string>? Context { get; set; }

        [Input("excessCapacityTerminationPolicy")]
        public Input<Pulumi.AwsNative.EC2.EC2FleetExcessCapacityTerminationPolicy>? ExcessCapacityTerminationPolicy { get; set; }

        [Input("launchTemplateConfigs", required: true)]
        private InputList<Inputs.EC2FleetFleetLaunchTemplateConfigRequestArgs>? _launchTemplateConfigs;
        public InputList<Inputs.EC2FleetFleetLaunchTemplateConfigRequestArgs> LaunchTemplateConfigs
        {
            get => _launchTemplateConfigs ?? (_launchTemplateConfigs = new InputList<Inputs.EC2FleetFleetLaunchTemplateConfigRequestArgs>());
            set => _launchTemplateConfigs = value;
        }

        [Input("onDemandOptions")]
        public Input<Inputs.EC2FleetOnDemandOptionsRequestArgs>? OnDemandOptions { get; set; }

        [Input("replaceUnhealthyInstances")]
        public Input<bool>? ReplaceUnhealthyInstances { get; set; }

        [Input("spotOptions")]
        public Input<Inputs.EC2FleetSpotOptionsRequestArgs>? SpotOptions { get; set; }

        [Input("tagSpecifications")]
        private InputList<Inputs.EC2FleetTagSpecificationArgs>? _tagSpecifications;
        public InputList<Inputs.EC2FleetTagSpecificationArgs> TagSpecifications
        {
            get => _tagSpecifications ?? (_tagSpecifications = new InputList<Inputs.EC2FleetTagSpecificationArgs>());
            set => _tagSpecifications = value;
        }

        [Input("targetCapacitySpecification", required: true)]
        public Input<Inputs.EC2FleetTargetCapacitySpecificationRequestArgs> TargetCapacitySpecification { get; set; } = null!;

        [Input("terminateInstancesWithExpiration")]
        public Input<bool>? TerminateInstancesWithExpiration { get; set; }

        [Input("type")]
        public Input<Pulumi.AwsNative.EC2.EC2FleetType>? Type { get; set; }

        [Input("validFrom")]
        public Input<string>? ValidFrom { get; set; }

        [Input("validUntil")]
        public Input<string>? ValidUntil { get; set; }

        public EC2FleetArgs()
        {
        }
        public static new EC2FleetArgs Empty => new EC2FleetArgs();
    }
}
