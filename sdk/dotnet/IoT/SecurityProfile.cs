// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoT
{
    /// <summary>
    /// A security profile defines a set of expected behaviors for devices in your account.
    /// </summary>
    [AwsNativeResourceType("aws-native:iot:SecurityProfile")]
    public partial class SecurityProfile : global::Pulumi.CustomResource
    {
        /// <summary>
        /// A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile's behaviors, but it is also retained for any metric specified here.
        /// </summary>
        [Output("additionalMetricsToRetainV2")]
        public Output<ImmutableArray<Outputs.SecurityProfileMetricToRetain>> AdditionalMetricsToRetainV2 { get; private set; } = null!;

        /// <summary>
        /// Specifies the destinations to which alerts are sent.
        /// </summary>
        [Output("alertTargets")]
        public Output<object?> AlertTargets { get; private set; } = null!;

        /// <summary>
        /// Specifies the behaviors that, when violated by a device (thing), cause an alert.
        /// </summary>
        [Output("behaviors")]
        public Output<ImmutableArray<Outputs.SecurityProfileBehavior>> Behaviors { get; private set; } = null!;

        /// <summary>
        /// A structure containing the mqtt topic for metrics export.
        /// </summary>
        [Output("metricsExportConfig")]
        public Output<Outputs.MetricsExportConfigProperties?> MetricsExportConfig { get; private set; } = null!;

        /// <summary>
        /// The ARN (Amazon resource name) of the created security profile.
        /// </summary>
        [Output("securityProfileArn")]
        public Output<string> SecurityProfileArn { get; private set; } = null!;

        /// <summary>
        /// A description of the security profile.
        /// </summary>
        [Output("securityProfileDescription")]
        public Output<string?> SecurityProfileDescription { get; private set; } = null!;

        /// <summary>
        /// A unique identifier for the security profile.
        /// </summary>
        [Output("securityProfileName")]
        public Output<string?> SecurityProfileName { get; private set; } = null!;

        /// <summary>
        /// Metadata that can be used to manage the security profile.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.SecurityProfileTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// A set of target ARNs that the security profile is attached to.
        /// </summary>
        [Output("targetArns")]
        public Output<ImmutableArray<string>> TargetArns { get; private set; } = null!;


        /// <summary>
        /// Create a SecurityProfile resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SecurityProfile(string name, SecurityProfileArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:iot:SecurityProfile", name, args ?? new SecurityProfileArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SecurityProfile(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:iot:SecurityProfile", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "securityProfileName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing SecurityProfile resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SecurityProfile Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new SecurityProfile(name, id, options);
        }
    }

    public sealed class SecurityProfileArgs : global::Pulumi.ResourceArgs
    {
        [Input("additionalMetricsToRetainV2")]
        private InputList<Inputs.SecurityProfileMetricToRetainArgs>? _additionalMetricsToRetainV2;

        /// <summary>
        /// A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile's behaviors, but it is also retained for any metric specified here.
        /// </summary>
        public InputList<Inputs.SecurityProfileMetricToRetainArgs> AdditionalMetricsToRetainV2
        {
            get => _additionalMetricsToRetainV2 ?? (_additionalMetricsToRetainV2 = new InputList<Inputs.SecurityProfileMetricToRetainArgs>());
            set => _additionalMetricsToRetainV2 = value;
        }

        /// <summary>
        /// Specifies the destinations to which alerts are sent.
        /// </summary>
        [Input("alertTargets")]
        public Input<object>? AlertTargets { get; set; }

        [Input("behaviors")]
        private InputList<Inputs.SecurityProfileBehaviorArgs>? _behaviors;

        /// <summary>
        /// Specifies the behaviors that, when violated by a device (thing), cause an alert.
        /// </summary>
        public InputList<Inputs.SecurityProfileBehaviorArgs> Behaviors
        {
            get => _behaviors ?? (_behaviors = new InputList<Inputs.SecurityProfileBehaviorArgs>());
            set => _behaviors = value;
        }

        /// <summary>
        /// A structure containing the mqtt topic for metrics export.
        /// </summary>
        [Input("metricsExportConfig")]
        public Input<Inputs.MetricsExportConfigPropertiesArgs>? MetricsExportConfig { get; set; }

        /// <summary>
        /// A description of the security profile.
        /// </summary>
        [Input("securityProfileDescription")]
        public Input<string>? SecurityProfileDescription { get; set; }

        /// <summary>
        /// A unique identifier for the security profile.
        /// </summary>
        [Input("securityProfileName")]
        public Input<string>? SecurityProfileName { get; set; }

        [Input("tags")]
        private InputList<Inputs.SecurityProfileTagArgs>? _tags;

        /// <summary>
        /// Metadata that can be used to manage the security profile.
        /// </summary>
        public InputList<Inputs.SecurityProfileTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.SecurityProfileTagArgs>());
            set => _tags = value;
        }

        [Input("targetArns")]
        private InputList<string>? _targetArns;

        /// <summary>
        /// A set of target ARNs that the security profile is attached to.
        /// </summary>
        public InputList<string> TargetArns
        {
            get => _targetArns ?? (_targetArns = new InputList<string>());
            set => _targetArns = value;
        }

        public SecurityProfileArgs()
        {
        }
        public static new SecurityProfileArgs Empty => new SecurityProfileArgs();
    }
}
