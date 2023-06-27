// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Backup.Inputs
{

    public sealed class BackupPlanBackupRuleResourceTypeArgs : global::Pulumi.ResourceArgs
    {
        [Input("completionWindowMinutes")]
        public Input<double>? CompletionWindowMinutes { get; set; }

        [Input("copyActions")]
        private InputList<Inputs.BackupPlanCopyActionResourceTypeArgs>? _copyActions;
        public InputList<Inputs.BackupPlanCopyActionResourceTypeArgs> CopyActions
        {
            get => _copyActions ?? (_copyActions = new InputList<Inputs.BackupPlanCopyActionResourceTypeArgs>());
            set => _copyActions = value;
        }

        [Input("enableContinuousBackup")]
        public Input<bool>? EnableContinuousBackup { get; set; }

        [Input("lifecycle")]
        public Input<Inputs.BackupPlanLifecycleResourceTypeArgs>? Lifecycle { get; set; }

        [Input("recoveryPointTags")]
        public Input<object>? RecoveryPointTags { get; set; }

        [Input("ruleName", required: true)]
        public Input<string> RuleName { get; set; } = null!;

        [Input("scheduleExpression")]
        public Input<string>? ScheduleExpression { get; set; }

        [Input("startWindowMinutes")]
        public Input<double>? StartWindowMinutes { get; set; }

        [Input("targetBackupVault", required: true)]
        public Input<string> TargetBackupVault { get; set; } = null!;

        public BackupPlanBackupRuleResourceTypeArgs()
        {
        }
        public static new BackupPlanBackupRuleResourceTypeArgs Empty => new BackupPlanBackupRuleResourceTypeArgs();
    }
}
