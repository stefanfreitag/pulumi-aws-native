// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.FSx.Inputs
{

    public sealed class FileSystemLustreConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("autoImportPolicy")]
        public Input<string>? AutoImportPolicy { get; set; }

        [Input("automaticBackupRetentionDays")]
        public Input<int>? AutomaticBackupRetentionDays { get; set; }

        [Input("copyTagsToBackups")]
        public Input<bool>? CopyTagsToBackups { get; set; }

        [Input("dailyAutomaticBackupStartTime")]
        public Input<string>? DailyAutomaticBackupStartTime { get; set; }

        [Input("dataCompressionType")]
        public Input<string>? DataCompressionType { get; set; }

        [Input("deploymentType")]
        public Input<string>? DeploymentType { get; set; }

        [Input("driveCacheType")]
        public Input<string>? DriveCacheType { get; set; }

        [Input("exportPath")]
        public Input<string>? ExportPath { get; set; }

        [Input("importPath")]
        public Input<string>? ImportPath { get; set; }

        [Input("importedFileChunkSize")]
        public Input<int>? ImportedFileChunkSize { get; set; }

        [Input("perUnitStorageThroughput")]
        public Input<int>? PerUnitStorageThroughput { get; set; }

        [Input("weeklyMaintenanceStartTime")]
        public Input<string>? WeeklyMaintenanceStartTime { get; set; }

        public FileSystemLustreConfigurationArgs()
        {
        }
        public static new FileSystemLustreConfigurationArgs Empty => new FileSystemLustreConfigurationArgs();
    }
}
