// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DMS.Outputs
{

    [OutputType]
    public sealed class EndpointOracleSettings
    {
        public readonly bool? AccessAlternateDirectly;
        public readonly bool? AddSupplementalLogging;
        public readonly int? AdditionalArchivedLogDestId;
        public readonly bool? AllowSelectNestedTables;
        public readonly int? ArchivedLogDestId;
        public readonly bool? ArchivedLogsOnly;
        public readonly string? AsmPassword;
        public readonly string? AsmServer;
        public readonly string? AsmUser;
        public readonly string? CharLengthSemantics;
        public readonly bool? DirectPathNoLog;
        public readonly bool? DirectPathParallelLoad;
        public readonly bool? EnableHomogenousTablespace;
        public readonly ImmutableArray<int> ExtraArchivedLogDestIds;
        public readonly bool? FailTasksOnLobTruncation;
        public readonly int? NumberDatatypeScale;
        public readonly string? OraclePathPrefix;
        public readonly int? ParallelAsmReadThreads;
        public readonly int? ReadAheadBlocks;
        public readonly bool? ReadTableSpaceName;
        public readonly bool? ReplacePathPrefix;
        public readonly int? RetryInterval;
        public readonly string? SecretsManagerAccessRoleArn;
        public readonly string? SecretsManagerOracleAsmAccessRoleArn;
        public readonly string? SecretsManagerOracleAsmSecretId;
        public readonly string? SecretsManagerSecretId;
        public readonly string? SecurityDbEncryption;
        public readonly string? SecurityDbEncryptionName;
        public readonly string? SpatialDataOptionToGeoJsonFunctionName;
        public readonly int? StandbyDelayTime;
        public readonly bool? UseAlternateFolderForOnline;
        public readonly bool? UseBFile;
        public readonly bool? UseDirectPathFullLoad;
        public readonly bool? UseLogminerReader;
        public readonly string? UsePathPrefix;

        [OutputConstructor]
        private EndpointOracleSettings(
            bool? accessAlternateDirectly,

            bool? addSupplementalLogging,

            int? additionalArchivedLogDestId,

            bool? allowSelectNestedTables,

            int? archivedLogDestId,

            bool? archivedLogsOnly,

            string? asmPassword,

            string? asmServer,

            string? asmUser,

            string? charLengthSemantics,

            bool? directPathNoLog,

            bool? directPathParallelLoad,

            bool? enableHomogenousTablespace,

            ImmutableArray<int> extraArchivedLogDestIds,

            bool? failTasksOnLobTruncation,

            int? numberDatatypeScale,

            string? oraclePathPrefix,

            int? parallelAsmReadThreads,

            int? readAheadBlocks,

            bool? readTableSpaceName,

            bool? replacePathPrefix,

            int? retryInterval,

            string? secretsManagerAccessRoleArn,

            string? secretsManagerOracleAsmAccessRoleArn,

            string? secretsManagerOracleAsmSecretId,

            string? secretsManagerSecretId,

            string? securityDbEncryption,

            string? securityDbEncryptionName,

            string? spatialDataOptionToGeoJsonFunctionName,

            int? standbyDelayTime,

            bool? useAlternateFolderForOnline,

            bool? useBFile,

            bool? useDirectPathFullLoad,

            bool? useLogminerReader,

            string? usePathPrefix)
        {
            AccessAlternateDirectly = accessAlternateDirectly;
            AddSupplementalLogging = addSupplementalLogging;
            AdditionalArchivedLogDestId = additionalArchivedLogDestId;
            AllowSelectNestedTables = allowSelectNestedTables;
            ArchivedLogDestId = archivedLogDestId;
            ArchivedLogsOnly = archivedLogsOnly;
            AsmPassword = asmPassword;
            AsmServer = asmServer;
            AsmUser = asmUser;
            CharLengthSemantics = charLengthSemantics;
            DirectPathNoLog = directPathNoLog;
            DirectPathParallelLoad = directPathParallelLoad;
            EnableHomogenousTablespace = enableHomogenousTablespace;
            ExtraArchivedLogDestIds = extraArchivedLogDestIds;
            FailTasksOnLobTruncation = failTasksOnLobTruncation;
            NumberDatatypeScale = numberDatatypeScale;
            OraclePathPrefix = oraclePathPrefix;
            ParallelAsmReadThreads = parallelAsmReadThreads;
            ReadAheadBlocks = readAheadBlocks;
            ReadTableSpaceName = readTableSpaceName;
            ReplacePathPrefix = replacePathPrefix;
            RetryInterval = retryInterval;
            SecretsManagerAccessRoleArn = secretsManagerAccessRoleArn;
            SecretsManagerOracleAsmAccessRoleArn = secretsManagerOracleAsmAccessRoleArn;
            SecretsManagerOracleAsmSecretId = secretsManagerOracleAsmSecretId;
            SecretsManagerSecretId = secretsManagerSecretId;
            SecurityDbEncryption = securityDbEncryption;
            SecurityDbEncryptionName = securityDbEncryptionName;
            SpatialDataOptionToGeoJsonFunctionName = spatialDataOptionToGeoJsonFunctionName;
            StandbyDelayTime = standbyDelayTime;
            UseAlternateFolderForOnline = useAlternateFolderForOnline;
            UseBFile = useBFile;
            UseDirectPathFullLoad = useDirectPathFullLoad;
            UseLogminerReader = useLogminerReader;
            UsePathPrefix = usePathPrefix;
        }
    }
}
