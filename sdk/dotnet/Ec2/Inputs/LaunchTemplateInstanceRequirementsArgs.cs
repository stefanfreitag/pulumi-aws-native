// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2.Inputs
{

    /// <summary>
    /// The attributes for the instance types.
    /// </summary>
    public sealed class LaunchTemplateInstanceRequirementsArgs : global::Pulumi.ResourceArgs
    {
        [Input("acceleratorCount")]
        public Input<Inputs.LaunchTemplateAcceleratorCountArgs>? AcceleratorCount { get; set; }

        [Input("acceleratorManufacturers")]
        private InputList<string>? _acceleratorManufacturers;

        /// <summary>
        /// Indicates whether instance types must have accelerators by specific manufacturers.
        /// </summary>
        public InputList<string> AcceleratorManufacturers
        {
            get => _acceleratorManufacturers ?? (_acceleratorManufacturers = new InputList<string>());
            set => _acceleratorManufacturers = value;
        }

        [Input("acceleratorNames")]
        private InputList<string>? _acceleratorNames;

        /// <summary>
        /// The accelerators that must be on the instance type.
        /// </summary>
        public InputList<string> AcceleratorNames
        {
            get => _acceleratorNames ?? (_acceleratorNames = new InputList<string>());
            set => _acceleratorNames = value;
        }

        [Input("acceleratorTotalMemoryMiB")]
        public Input<Inputs.LaunchTemplateAcceleratorTotalMemoryMiBArgs>? AcceleratorTotalMemoryMiB { get; set; }

        [Input("acceleratorTypes")]
        private InputList<string>? _acceleratorTypes;

        /// <summary>
        /// The accelerator types that must be on the instance type.
        /// </summary>
        public InputList<string> AcceleratorTypes
        {
            get => _acceleratorTypes ?? (_acceleratorTypes = new InputList<string>());
            set => _acceleratorTypes = value;
        }

        [Input("allowedInstanceTypes")]
        private InputList<string>? _allowedInstanceTypes;

        /// <summary>
        /// The instance types to apply your specified attributes against.
        /// </summary>
        public InputList<string> AllowedInstanceTypes
        {
            get => _allowedInstanceTypes ?? (_allowedInstanceTypes = new InputList<string>());
            set => _allowedInstanceTypes = value;
        }

        /// <summary>
        /// Indicates whether bare metal instance types must be included, excluded, or required.
        /// </summary>
        [Input("bareMetal")]
        public Input<string>? BareMetal { get; set; }

        [Input("baselineEbsBandwidthMbps")]
        public Input<Inputs.LaunchTemplateBaselineEbsBandwidthMbpsArgs>? BaselineEbsBandwidthMbps { get; set; }

        [Input("burstablePerformance")]
        public Input<string>? BurstablePerformance { get; set; }

        [Input("cpuManufacturers")]
        private InputList<string>? _cpuManufacturers;

        /// <summary>
        /// The CPU manufacturers to include.
        /// </summary>
        public InputList<string> CpuManufacturers
        {
            get => _cpuManufacturers ?? (_cpuManufacturers = new InputList<string>());
            set => _cpuManufacturers = value;
        }

        [Input("excludedInstanceTypes")]
        private InputList<string>? _excludedInstanceTypes;

        /// <summary>
        /// The instance types to exclude.
        /// </summary>
        public InputList<string> ExcludedInstanceTypes
        {
            get => _excludedInstanceTypes ?? (_excludedInstanceTypes = new InputList<string>());
            set => _excludedInstanceTypes = value;
        }

        [Input("instanceGenerations")]
        private InputList<string>? _instanceGenerations;

        /// <summary>
        /// Indicates whether current or previous generation instance types are included.
        /// </summary>
        public InputList<string> InstanceGenerations
        {
            get => _instanceGenerations ?? (_instanceGenerations = new InputList<string>());
            set => _instanceGenerations = value;
        }

        /// <summary>
        /// The user data to make available to the instance.
        /// </summary>
        [Input("localStorage")]
        public Input<string>? LocalStorage { get; set; }

        [Input("localStorageTypes")]
        private InputList<string>? _localStorageTypes;

        /// <summary>
        /// The type of local storage that is required.
        /// </summary>
        public InputList<string> LocalStorageTypes
        {
            get => _localStorageTypes ?? (_localStorageTypes = new InputList<string>());
            set => _localStorageTypes = value;
        }

        /// <summary>
        /// The price protection threshold for Spot Instances.
        /// </summary>
        [Input("maxSpotPriceAsPercentageOfOptimalOnDemandPrice")]
        public Input<int>? MaxSpotPriceAsPercentageOfOptimalOnDemandPrice { get; set; }

        [Input("memoryGiBPerVCpu")]
        public Input<Inputs.LaunchTemplateMemoryGiBPerVCpuArgs>? MemoryGiBPerVCpu { get; set; }

        [Input("memoryMiB")]
        public Input<Inputs.LaunchTemplateMemoryMiBArgs>? MemoryMiB { get; set; }

        [Input("networkBandwidthGbps")]
        public Input<Inputs.LaunchTemplateNetworkBandwidthGbpsArgs>? NetworkBandwidthGbps { get; set; }

        [Input("networkInterfaceCount")]
        public Input<Inputs.LaunchTemplateNetworkInterfaceCountArgs>? NetworkInterfaceCount { get; set; }

        /// <summary>
        /// The price protection threshold for On-Demand Instances.
        /// </summary>
        [Input("onDemandMaxPricePercentageOverLowestPrice")]
        public Input<int>? OnDemandMaxPricePercentageOverLowestPrice { get; set; }

        /// <summary>
        /// Indicates whether instance types must support hibernation for On-Demand Instances.
        /// </summary>
        [Input("requireHibernateSupport")]
        public Input<bool>? RequireHibernateSupport { get; set; }

        /// <summary>
        /// The price protection threshold for Spot Instances.
        /// </summary>
        [Input("spotMaxPricePercentageOverLowestPrice")]
        public Input<int>? SpotMaxPricePercentageOverLowestPrice { get; set; }

        [Input("totalLocalStorageGb")]
        public Input<Inputs.LaunchTemplateTotalLocalStorageGbArgs>? TotalLocalStorageGb { get; set; }

        [Input("vCpuCount")]
        public Input<Inputs.LaunchTemplateVCpuCountArgs>? VCpuCount { get; set; }

        public LaunchTemplateInstanceRequirementsArgs()
        {
        }
        public static new LaunchTemplateInstanceRequirementsArgs Empty => new LaunchTemplateInstanceRequirementsArgs();
    }
}
